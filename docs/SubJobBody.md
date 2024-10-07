# SubJobBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**sub_job** | [**SubJobBodySubJob**](SubJobBodySubJob.md) |  | 

## Example

```python
from procore_sdk.models.sub_job_body import SubJobBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubJobBody from a JSON string
sub_job_body_instance = SubJobBody.from_json(json)
# print the JSON string representation of the object
print(SubJobBody.to_json())

# convert the object into a dict
sub_job_body_dict = sub_job_body_instance.to_dict()
# create an instance of SubJobBody from a dict
sub_job_body_from_dict = SubJobBody.from_dict(sub_job_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


