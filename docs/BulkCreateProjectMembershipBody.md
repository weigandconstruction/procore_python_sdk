# BulkCreateProjectMembershipBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_ids** | **List[int]** |  | 

## Example

```python
from procore_sdk.models.bulk_create_project_membership_body import BulkCreateProjectMembershipBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateProjectMembershipBody from a JSON string
bulk_create_project_membership_body_instance = BulkCreateProjectMembershipBody.from_json(json)
# print the JSON string representation of the object
print(BulkCreateProjectMembershipBody.to_json())

# convert the object into a dict
bulk_create_project_membership_body_dict = bulk_create_project_membership_body_instance.to_dict()
# create an instance of BulkCreateProjectMembershipBody from a dict
bulk_create_project_membership_body_from_dict = BulkCreateProjectMembershipBody.from_dict(bulk_create_project_membership_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


