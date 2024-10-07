# CorrespondenceRecipientsInnerInner

Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachments ID | [optional] 
**name** | **str** | Name of attachment | [optional] 
**url** | **str** | Link to attachment | [optional] 
**filename** | **str** | Filename | [optional] 

## Example

```python
from procore_sdk.models.correspondence_recipients_inner_inner import CorrespondenceRecipientsInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of CorrespondenceRecipientsInnerInner from a JSON string
correspondence_recipients_inner_inner_instance = CorrespondenceRecipientsInnerInner.from_json(json)
# print the JSON string representation of the object
print(CorrespondenceRecipientsInnerInner.to_json())

# convert the object into a dict
correspondence_recipients_inner_inner_dict = correspondence_recipients_inner_inner_instance.to_dict()
# create an instance of CorrespondenceRecipientsInnerInner from a dict
correspondence_recipients_inner_inner_from_dict = CorrespondenceRecipientsInnerInner.from_dict(correspondence_recipients_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


