# ArrayOfDirectCostItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10ProjectsProjectIdDirectCostsPost201Response]**](RestV10ProjectsProjectIdDirectCostsPost201Response.md) |  | [optional] 
**errors** | [**List[ArrayOfDirectCostItemsErrorsInner]**](ArrayOfDirectCostItemsErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_direct_cost_items import ArrayOfDirectCostItems

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDirectCostItems from a JSON string
array_of_direct_cost_items_instance = ArrayOfDirectCostItems.from_json(json)
# print the JSON string representation of the object
print(ArrayOfDirectCostItems.to_json())

# convert the object into a dict
array_of_direct_cost_items_dict = array_of_direct_cost_items_instance.to_dict()
# create an instance of ArrayOfDirectCostItems from a dict
array_of_direct_cost_items_from_dict = ArrayOfDirectCostItems.from_dict(array_of_direct_cost_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


