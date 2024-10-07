# WorkActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Work Activity ID | [optional] 
**name** | **str** | Work Activity Name | [optional] 
**active** | **bool** | Represents whether a Work Activity is available for use. | [optional] 
**var_global** | **bool** | Represents whether a Work Activity has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Date the work activity was updated | [optional] 

## Example

```python
from procore_sdk.models.work_activity import WorkActivity

# TODO update the JSON string below
json = "{}"
# create an instance of WorkActivity from a JSON string
work_activity_instance = WorkActivity.from_json(json)
# print the JSON string representation of the object
print(WorkActivity.to_json())

# convert the object into a dict
work_activity_dict = work_activity_instance.to_dict()
# create an instance of WorkActivity from a dict
work_activity_from_dict = WorkActivity.from_dict(work_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


