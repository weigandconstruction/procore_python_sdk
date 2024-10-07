# MeetingTopic

Meeting topic object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The Title of the Meeting Topic | [optional] 
**description** | **str** | The Description of the Meeting Topic | [optional] 
**due_date** | **date** | The Due Date of the Meeting Topic | [optional] 
**status** | **str** | The Status of the Meeting Topic | [optional] 
**minutes** | **str** | &lt;p&gt;&lt;span style&#x3D;\\\\\\\&quot;font-size: large;\\\\\\\&quot;&gt;Please look at Item 1 and have those pieces completed &lt;strong&gt;before&lt;/strong&gt;&lt;/span&gt;&lt;/p&gt; | [optional] 
**is_private** | **bool** | The Private status of the Meeting Topic | [optional] 
**closed_at** | **datetime** | The Date of the Meeting Topic being closed | [optional] 
**priority** | **str** | The Priority of the Meeting Topic | [optional] 
**added_under_agenda** | **bool** | The Added Under Agenda status of the Meeting Topic | [optional] [default to True]
**meeting_wide_number** | **int** | The Meeting Wide Number of the Meeting Topic | [optional] 
**meeting_category_id** | **int** | The ID of the Meeting Category the Meeting Topic belongs to | [optional] 
**assignment_ids** | [**List[MeetingTopicAssignmentIdsInner]**](MeetingTopicAssignmentIdsInner.md) | An array of the IDs of the Assignments of the Meeting Topic.  Setting &#x60;meeting_topic[assignment_ids]&#x60; to \&quot;none\&quot; erases assignments. | [optional] 

## Example

```python
from procore_sdk.models.meeting_topic import MeetingTopic

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingTopic from a JSON string
meeting_topic_instance = MeetingTopic.from_json(json)
# print the JSON string representation of the object
print(MeetingTopic.to_json())

# convert the object into a dict
meeting_topic_dict = meeting_topic_instance.to_dict()
# create an instance of MeetingTopic from a dict
meeting_topic_from_dict = MeetingTopic.from_dict(meeting_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


