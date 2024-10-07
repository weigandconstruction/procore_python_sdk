# Checklist3AttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**filename** | **str** | Filename | [optional] 
**name** | **str** | Filename | [optional] 

## Example

```python
from procore_sdk.models.checklist3_attachments_inner import Checklist3AttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist3AttachmentsInner from a JSON string
checklist3_attachments_inner_instance = Checklist3AttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(Checklist3AttachmentsInner.to_json())

# convert the object into a dict
checklist3_attachments_inner_dict = checklist3_attachments_inner_instance.to_dict()
# create an instance of Checklist3AttachmentsInner from a dict
checklist3_attachments_inner_from_dict = Checklist3AttachmentsInner.from_dict(checklist3_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


