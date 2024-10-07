# NormalViewAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**name** | **str** | Filename | [optional] 
**filename** | **str** | Filename | [optional] 

## Example

```python
from procore_sdk.models.normal_view_attachments_inner import NormalViewAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NormalViewAttachmentsInner from a JSON string
normal_view_attachments_inner_instance = NormalViewAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(NormalViewAttachmentsInner.to_json())

# convert the object into a dict
normal_view_attachments_inner_dict = normal_view_attachments_inner_instance.to_dict()
# create an instance of NormalViewAttachmentsInner from a dict
normal_view_attachments_inner_from_dict = NormalViewAttachmentsInner.from_dict(normal_view_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


