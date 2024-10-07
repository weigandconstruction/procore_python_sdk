# ProjectPersistentMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Project persistent message | [optional] 
**title** | **str** | Project persistent message title | [optional] 

## Example

```python
from procore_sdk.models.project_persistent_message import ProjectPersistentMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPersistentMessage from a JSON string
project_persistent_message_instance = ProjectPersistentMessage.from_json(json)
# print the JSON string representation of the object
print(ProjectPersistentMessage.to_json())

# convert the object into a dict
project_persistent_message_dict = project_persistent_message_instance.to_dict()
# create an instance of ProjectPersistentMessage from a dict
project_persistent_message_from_dict = ProjectPersistentMessage.from_dict(project_persistent_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


