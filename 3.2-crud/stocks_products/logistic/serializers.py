from rest_framework import serializers

from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']



class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        # Создание записей в связанной таблице StockProduct:
        for pos in positions:
            new_pos = StockProduct(stock=stock, **pos)
            new_pos.save()

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        pos_list = instance.positions.all()
        pos_list = list(pos_list)

        stock = super().update(instance, validated_data)

        # Обновление записей в связанной таблице StockProduct:
        for position in positions:
            pos_update = pos_list.pop(0)
            pos_update.product = position.get('product', pos_update.product)
            pos_update.quantity = position.get('quantity', pos_update.quantity)
            pos_update.price = position.get('price', pos_update.price)
            pos_update.save()

        return stock
