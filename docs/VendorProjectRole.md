# VendorProjectRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Role ID | [optional] 
**vendor_ids** | **List[int]** | Array of Vendor IDs associated with the Project Role | [optional] 

## Example

```python
from procore_sdk.models.vendor_project_role import VendorProjectRole

# TODO update the JSON string below
json = "{}"
# create an instance of VendorProjectRole from a JSON string
vendor_project_role_instance = VendorProjectRole.from_json(json)
# print the JSON string representation of the object
print(VendorProjectRole.to_json())

# convert the object into a dict
vendor_project_role_dict = vendor_project_role_instance.to_dict()
# create an instance of VendorProjectRole from a dict
vendor_project_role_from_dict = VendorProjectRole.from_dict(vendor_project_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


