# ArrayOfPotentialChangeOrderLineItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Default]**](Default.md) |  | [optional] 
**errors** | [**List[ArrayOfPotentialChangeOrderLineItemsErrorsInner]**](ArrayOfPotentialChangeOrderLineItemsErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_potential_change_order_line_items import ArrayOfPotentialChangeOrderLineItems

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPotentialChangeOrderLineItems from a JSON string
array_of_potential_change_order_line_items_instance = ArrayOfPotentialChangeOrderLineItems.from_json(json)
# print the JSON string representation of the object
print(ArrayOfPotentialChangeOrderLineItems.to_json())

# convert the object into a dict
array_of_potential_change_order_line_items_dict = array_of_potential_change_order_line_items_instance.to_dict()
# create an instance of ArrayOfPotentialChangeOrderLineItems from a dict
array_of_potential_change_order_line_items_from_dict = ArrayOfPotentialChangeOrderLineItems.from_dict(array_of_potential_change_order_line_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


