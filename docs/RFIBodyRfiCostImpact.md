# RFIBodyRfiCostImpact

The Cost Impact of the RFI

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The Status of the Cost Impact | [optional] 
**value** | **float** | Cost impact value in dollars | [optional] 

## Example

```python
from procore_sdk.models.rfi_body_rfi_cost_impact import RFIBodyRfiCostImpact

# TODO update the JSON string below
json = "{}"
# create an instance of RFIBodyRfiCostImpact from a JSON string
rfi_body_rfi_cost_impact_instance = RFIBodyRfiCostImpact.from_json(json)
# print the JSON string representation of the object
print(RFIBodyRfiCostImpact.to_json())

# convert the object into a dict
rfi_body_rfi_cost_impact_dict = rfi_body_rfi_cost_impact_instance.to_dict()
# create an instance of RFIBodyRfiCostImpact from a dict
rfi_body_rfi_cost_impact_from_dict = RFIBodyRfiCostImpact.from_dict(rfi_body_rfi_cost_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


