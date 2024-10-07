# PunchItemCommentCreator

User that created the Punch Item Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | User Name | [optional] 
**login** | **str** | User Email | [optional] 
**company_name** | **str** | Name of the User&#39;s Company | [optional] 

## Example

```python
from procore_sdk.models.punch_item_comment_creator import PunchItemCommentCreator

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemCommentCreator from a JSON string
punch_item_comment_creator_instance = PunchItemCommentCreator.from_json(json)
# print the JSON string representation of the object
print(PunchItemCommentCreator.to_json())

# convert the object into a dict
punch_item_comment_creator_dict = punch_item_comment_creator_instance.to_dict()
# create an instance of PunchItemCommentCreator from a dict
punch_item_comment_creator_from_dict = PunchItemCommentCreator.from_dict(punch_item_comment_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


