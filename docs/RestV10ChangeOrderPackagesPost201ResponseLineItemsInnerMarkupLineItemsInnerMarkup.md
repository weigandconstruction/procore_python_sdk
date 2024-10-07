# RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Markup ID | [optional] 
**position** | **int** | Position | [optional] 
**markup_set** | **str** | Markup set | [optional] 
**name** | **str** | name | [optional] 
**percentage** | **str** | Percentage | [optional] 
**compounds_markups_above** | **bool** | Compounds markups above? | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**destination_cost_code** | [**RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode**](RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode.md) |  | [optional] 
**destination_line_item_type** | [**LineItemType3**](LineItemType3.md) |  | [optional] 
**desitination_budget_line_item_id** | **int** | Destination Budget Line Item ID | [optional] 
**destination_sub_job** | [**RestV10SubJobsGet200ResponseInner**](RestV10SubJobsGet200ResponseInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_packages_post201_response_line_items_inner_markup_line_items_inner_markup import RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup from a JSON string
rest_v10_change_order_packages_post201_response_line_items_inner_markup_line_items_inner_markup_instance = RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup.to_json())

# convert the object into a dict
rest_v10_change_order_packages_post201_response_line_items_inner_markup_line_items_inner_markup_dict = rest_v10_change_order_packages_post201_response_line_items_inner_markup_line_items_inner_markup_instance.to_dict()
# create an instance of RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup from a dict
rest_v10_change_order_packages_post201_response_line_items_inner_markup_line_items_inner_markup_from_dict = RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInnerMarkup.from_dict(rest_v10_change_order_packages_post201_response_line_items_inner_markup_line_items_inner_markup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


