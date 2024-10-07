# ProjectMembership

Project Membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Membership id | [optional] 
**party_id** | **int** | Party id | [optional] 
**project_id** | **int** | Project id | [optional] 

## Example

```python
from procore_sdk.models.project_membership import ProjectMembership

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembership from a JSON string
project_membership_instance = ProjectMembership.from_json(json)
# print the JSON string representation of the object
print(ProjectMembership.to_json())

# convert the object into a dict
project_membership_dict = project_membership_instance.to_dict()
# create an instance of ProjectMembership from a dict
project_membership_from_dict = ProjectMembership.from_dict(project_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


