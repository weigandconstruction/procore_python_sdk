# RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Markup Line Item ID | [optional] 
**amount** | **str** | Markup Line Item amount | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**markup** | [**RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInnerMarkup**](RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInnerMarkup.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_packages_id_get200_response_line_items_inner_markup_line_items_inner import RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInner from a JSON string
rest_v10_change_order_packages_id_get200_response_line_items_inner_markup_line_items_inner_instance = RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInner.to_json())

# convert the object into a dict
rest_v10_change_order_packages_id_get200_response_line_items_inner_markup_line_items_inner_dict = rest_v10_change_order_packages_id_get200_response_line_items_inner_markup_line_items_inner_instance.to_dict()
# create an instance of RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInner from a dict
rest_v10_change_order_packages_id_get200_response_line_items_inner_markup_line_items_inner_from_dict = RestV10ChangeOrderPackagesIdGet200ResponseLineItemsInnerMarkupLineItemsInner.from_dict(rest_v10_change_order_packages_id_get200_response_line_items_inner_markup_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


