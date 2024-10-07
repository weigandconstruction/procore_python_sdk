# UserProjectRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Role ID | [optional] 
**user_ids** | **List[int]** | Array of User IDs associated with the Project Role | [optional] 

## Example

```python
from procore_sdk.models.user_project_role import UserProjectRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserProjectRole from a JSON string
user_project_role_instance = UserProjectRole.from_json(json)
# print the JSON string representation of the object
print(UserProjectRole.to_json())

# convert the object into a dict
user_project_role_dict = user_project_role_instance.to_dict()
# create an instance of UserProjectRole from a dict
user_project_role_from_dict = UserProjectRole.from_dict(user_project_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


