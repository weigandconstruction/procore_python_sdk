# GenericToolItem1CostImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Cost impact status | [optional] 
**value** | **float** | Cost impact value in dollars | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item1_cost_impact import GenericToolItem1CostImpact

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItem1CostImpact from a JSON string
generic_tool_item1_cost_impact_instance = GenericToolItem1CostImpact.from_json(json)
# print the JSON string representation of the object
print(GenericToolItem1CostImpact.to_json())

# convert the object into a dict
generic_tool_item1_cost_impact_dict = generic_tool_item1_cost_impact_instance.to_dict()
# create an instance of GenericToolItem1CostImpact from a dict
generic_tool_item1_cost_impact_from_dict = GenericToolItem1CostImpact.from_dict(generic_tool_item1_cost_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


