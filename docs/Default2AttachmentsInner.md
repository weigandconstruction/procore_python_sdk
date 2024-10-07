# Default2AttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**name** | **str** | Filename | [optional] 

## Example

```python
from procore_sdk.models.default2_attachments_inner import Default2AttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Default2AttachmentsInner from a JSON string
default2_attachments_inner_instance = Default2AttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(Default2AttachmentsInner.to_json())

# convert the object into a dict
default2_attachments_inner_dict = default2_attachments_inner_instance.to_dict()
# create an instance of Default2AttachmentsInner from a dict
default2_attachments_inner_from_dict = Default2AttachmentsInner.from_dict(default2_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


