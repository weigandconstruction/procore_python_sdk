# PunchItemCommentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**Comment1**](Comment1.md) |  | 
**attachments** | **List[str]** | Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.punch_item_comment_body import PunchItemCommentBody

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemCommentBody from a JSON string
punch_item_comment_body_instance = PunchItemCommentBody.from_json(json)
# print the JSON string representation of the object
print(PunchItemCommentBody.to_json())

# convert the object into a dict
punch_item_comment_body_dict = punch_item_comment_body_instance.to_dict()
# create an instance of PunchItemCommentBody from a dict
punch_item_comment_body_from_dict = PunchItemCommentBody.from_dict(punch_item_comment_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


