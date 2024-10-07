# Body127


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_plans** | [**List[Body125BimPlan]**](Body125BimPlan.md) | An array of BIM Plan payloads | 

## Example

```python
from procore_sdk.models.body127 import Body127

# TODO update the JSON string below
json = "{}"
# create an instance of Body127 from a JSON string
body127_instance = Body127.from_json(json)
# print the JSON string representation of the object
print(Body127.to_json())

# convert the object into a dict
body127_dict = body127_instance.to_dict()
# create an instance of Body127 from a dict
body127_from_dict = Body127.from_dict(body127_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


