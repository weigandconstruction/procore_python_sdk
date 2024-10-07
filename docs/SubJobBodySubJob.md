# SubJobBodySubJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**code** | **str** | Unique code in the scope of a Project | [optional] 
**origin_id** | **str** | The Third-party unique identifier of the Sub Job | [optional] 
**origin_data** | **str** | The Third-party Data of the Sub Job | [optional] 

## Example

```python
from procore_sdk.models.sub_job_body_sub_job import SubJobBodySubJob

# TODO update the JSON string below
json = "{}"
# create an instance of SubJobBodySubJob from a JSON string
sub_job_body_sub_job_instance = SubJobBodySubJob.from_json(json)
# print the JSON string representation of the object
print(SubJobBodySubJob.to_json())

# convert the object into a dict
sub_job_body_sub_job_dict = sub_job_body_sub_job_instance.to_dict()
# create an instance of SubJobBodySubJob from a dict
sub_job_body_sub_job_from_dict = SubJobBodySubJob.from_dict(sub_job_body_sub_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


