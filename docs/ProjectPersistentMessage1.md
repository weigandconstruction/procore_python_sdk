# ProjectPersistentMessage1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the persistent message for the Project | [optional] 
**message** | **str** | The text content for the Project persistent message | [optional] 

## Example

```python
from procore_sdk.models.project_persistent_message1 import ProjectPersistentMessage1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPersistentMessage1 from a JSON string
project_persistent_message1_instance = ProjectPersistentMessage1.from_json(json)
# print the JSON string representation of the object
print(ProjectPersistentMessage1.to_json())

# convert the object into a dict
project_persistent_message1_dict = project_persistent_message1_instance.to_dict()
# create an instance of ProjectPersistentMessage1 from a dict
project_persistent_message1_from_dict = ProjectPersistentMessage1.from_dict(project_persistent_message1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


