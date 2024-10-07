# VendorCommentCreatedBy

The creator of the Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**avatar_url** | **str** | The URL pointing to the user avatar. | [optional] 
**initials** | **str** | The initials of the user. | [optional] 

## Example

```python
from procore_sdk.models.vendor_comment_created_by import VendorCommentCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCommentCreatedBy from a JSON string
vendor_comment_created_by_instance = VendorCommentCreatedBy.from_json(json)
# print the JSON string representation of the object
print(VendorCommentCreatedBy.to_json())

# convert the object into a dict
vendor_comment_created_by_dict = vendor_comment_created_by_instance.to_dict()
# create an instance of VendorCommentCreatedBy from a dict
vendor_comment_created_by_from_dict = VendorCommentCreatedBy.from_dict(vendor_comment_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


