# ProjectVendorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | [**ProjectVendor**](ProjectVendor.md) |  | 

## Example

```python
from procore_sdk.models.project_vendor_body import ProjectVendorBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectVendorBody from a JSON string
project_vendor_body_instance = ProjectVendorBody.from_json(json)
# print the JSON string representation of the object
print(ProjectVendorBody.to_json())

# convert the object into a dict
project_vendor_body_dict = project_vendor_body_instance.to_dict()
# create an instance of ProjectVendorBody from a dict
project_vendor_body_from_dict = ProjectVendorBody.from_dict(project_vendor_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


