# ArrayOfDirectCostLineItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner]**](RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[ArrayOfPotentialChangeOrderLineItemsErrorsInner]**](ArrayOfPotentialChangeOrderLineItemsErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_direct_cost_line_items import ArrayOfDirectCostLineItems

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDirectCostLineItems from a JSON string
array_of_direct_cost_line_items_instance = ArrayOfDirectCostLineItems.from_json(json)
# print the JSON string representation of the object
print(ArrayOfDirectCostLineItems.to_json())

# convert the object into a dict
array_of_direct_cost_line_items_dict = array_of_direct_cost_line_items_instance.to_dict()
# create an instance of ArrayOfDirectCostLineItems from a dict
array_of_direct_cost_line_items_from_dict = ArrayOfDirectCostLineItems.from_dict(array_of_direct_cost_line_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


