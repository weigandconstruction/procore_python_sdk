# SubJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sub Job ID | [optional] 
**name** | **str** | Sub Job Name | [optional] 
**code** | **str** | Sub Job Code | [optional] 

## Example

```python
from procore_sdk.models.sub_job import SubJob

# TODO update the JSON string below
json = "{}"
# create an instance of SubJob from a JSON string
sub_job_instance = SubJob.from_json(json)
# print the JSON string representation of the object
print(SubJob.to_json())

# convert the object into a dict
sub_job_dict = sub_job_instance.to_dict()
# create an instance of SubJob from a dict
sub_job_from_dict = SubJob.from_dict(sub_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


