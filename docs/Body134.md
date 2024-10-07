# Body134


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_model_revision_plans** | [**List[Body133BimModelRevisionPlan]**](Body133BimModelRevisionPlan.md) | An array of BIM Model Revision Plan payloads | 

## Example

```python
from procore_sdk.models.body134 import Body134

# TODO update the JSON string below
json = "{}"
# create an instance of Body134 from a JSON string
body134_instance = Body134.from_json(json)
# print the JSON string representation of the object
print(Body134.to_json())

# convert the object into a dict
body134_dict = body134_instance.to_dict()
# create an instance of Body134 from a dict
body134_from_dict = Body134.from_dict(body134_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


