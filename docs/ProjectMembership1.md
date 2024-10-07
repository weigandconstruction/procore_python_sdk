# ProjectMembership1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_id** | **int** | The ID of the Party(reference user) to be added to the Project | 

## Example

```python
from procore_sdk.models.project_membership1 import ProjectMembership1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembership1 from a JSON string
project_membership1_instance = ProjectMembership1.from_json(json)
# print the JSON string representation of the object
print(ProjectMembership1.to_json())

# convert the object into a dict
project_membership1_dict = project_membership1_instance.to_dict()
# create an instance of ProjectMembership1 from a dict
project_membership1_from_dict = ProjectMembership1.from_dict(project_membership1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


