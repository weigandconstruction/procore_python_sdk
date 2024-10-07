# Body133BimModelRevisionPlan

BIM Model Revision Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_model_revision_id** | **int** | ID of BIM Model Revision | 
**bim_plan_id** | **int** | ID of BIM Plan. The BIM Plan should be associated to the same BIM File as the BIM Model Revision | 

## Example

```python
from procore_sdk.models.body133_bim_model_revision_plan import Body133BimModelRevisionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of Body133BimModelRevisionPlan from a JSON string
body133_bim_model_revision_plan_instance = Body133BimModelRevisionPlan.from_json(json)
# print the JSON string representation of the object
print(Body133BimModelRevisionPlan.to_json())

# convert the object into a dict
body133_bim_model_revision_plan_dict = body133_bim_model_revision_plan_instance.to_dict()
# create an instance of Body133BimModelRevisionPlan from a dict
body133_bim_model_revision_plan_from_dict = Body133BimModelRevisionPlan.from_dict(body133_bim_model_revision_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


