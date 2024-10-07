# ArrayOfPotentialChangeOrders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[ArrayOfPotentialChangeOrdersEntitiesInner]**](ArrayOfPotentialChangeOrdersEntitiesInner.md) |  | [optional] 
**errors** | [**List[ArrayOfPotentialChangeOrdersErrorsInner]**](ArrayOfPotentialChangeOrdersErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_potential_change_orders import ArrayOfPotentialChangeOrders

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPotentialChangeOrders from a JSON string
array_of_potential_change_orders_instance = ArrayOfPotentialChangeOrders.from_json(json)
# print the JSON string representation of the object
print(ArrayOfPotentialChangeOrders.to_json())

# convert the object into a dict
array_of_potential_change_orders_dict = array_of_potential_change_orders_instance.to_dict()
# create an instance of ArrayOfPotentialChangeOrders from a dict
array_of_potential_change_orders_from_dict = ArrayOfPotentialChangeOrders.from_dict(array_of_potential_change_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


