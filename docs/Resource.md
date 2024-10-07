# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Resource id | [optional] 
**company_id** | **int** | Company id | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**name** | **str** | Resource name | [optional] 
**project_id** | **int** | Project id | [optional] 
**schedule_attributes** | **Dict[str, str]** | When a schedule is imported from an external system, any attributes which are not otherwise represented in this object will appear as key-value pairs here. Note that the set of keys present in this object will depend on the application from which the schedule was obtained. | [optional] 
**source_uid** | **str** | The unique identifier for this resource from the external system which owns the schedule data. | [optional] 

## Example

```python
from procore_sdk.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


