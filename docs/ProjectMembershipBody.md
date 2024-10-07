# ProjectMembershipBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_membership** | [**ProjectMembership1**](ProjectMembership1.md) |  | 

## Example

```python
from procore_sdk.models.project_membership_body import ProjectMembershipBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembershipBody from a JSON string
project_membership_body_instance = ProjectMembershipBody.from_json(json)
# print the JSON string representation of the object
print(ProjectMembershipBody.to_json())

# convert the object into a dict
project_membership_body_dict = project_membership_body_instance.to_dict()
# create an instance of ProjectMembershipBody from a dict
project_membership_body_from_dict = ProjectMembershipBody.from_dict(project_membership_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


