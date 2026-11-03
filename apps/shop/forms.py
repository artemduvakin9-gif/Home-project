from django import forms 

class ProductForm(forms.Form):
    product_name = forms.CharField(
        max_length=200,
        label="Товар:",
        widget=forms.TextInput(attrs={
            'placeholder': "Максимальная длина 200 символов"
        })
    )

    text = forms.CharField(
        label = "Описание товара:",
        widget = forms.Textarea(attrs={
            'rows': 3,
            'cols': 20
        })
    )

    price = forms.DecimalField(
        label = "Цена товара:",
        widget = forms.NumberInput
    )

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name'].strip()

        if len(product_name) < 6:
            raise forms.ValidationError("Название не должно быть короче 6 символов")

        return product_name


    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError("укажите корректную цену товара")

        return price