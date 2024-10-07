# SubJobSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**updates** | [**List[SubJobSyncBodyUpdatesInner]**](SubJobSyncBodyUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.sub_job_sync_body import SubJobSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubJobSyncBody from a JSON string
sub_job_sync_body_instance = SubJobSyncBody.from_json(json)
# print the JSON string representation of the object
print(SubJobSyncBody.to_json())

# convert the object into a dict
sub_job_sync_body_dict = sub_job_sync_body_instance.to_dict()
# create an instance of SubJobSyncBody from a dict
sub_job_sync_body_from_dict = SubJobSyncBody.from_dict(sub_job_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


