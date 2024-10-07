# SeverityLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Name of the Incident Severity Level | [optional] 
**procore_default_name** | **str** | Procore default name of the Incident Severity Level | [optional] 
**active** | **bool** | Denotes whether the Incident Severity Level is active | [optional] 
**email_trigger** | **bool** | Denotes whether an email should be sent | [optional] 
**push_notification_trigger** | **bool** | Denotes whether a push notification should be sent | [optional] 
**order** | **int** | Ranking order of the Incident Severity Level | [optional] 
**created_at** | **datetime** | iso8601 timestamp of creation | [optional] 
**updated_at** | **datetime** | iso8601 timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.severity_level import SeverityLevel

# TODO update the JSON string below
json = "{}"
# create an instance of SeverityLevel from a JSON string
severity_level_instance = SeverityLevel.from_json(json)
# print the JSON string representation of the object
print(SeverityLevel.to_json())

# convert the object into a dict
severity_level_dict = severity_level_instance.to_dict()
# create an instance of SeverityLevel from a dict
severity_level_from_dict = SeverityLevel.from_dict(severity_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


