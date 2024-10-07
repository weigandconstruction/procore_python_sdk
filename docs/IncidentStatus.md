# IncidentStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The display value for the Incident status. | [optional] 
**value** | **str** | The value actually stored as the Incident status. | [optional] 

## Example

```python
from procore_sdk.models.incident_status import IncidentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentStatus from a JSON string
incident_status_instance = IncidentStatus.from_json(json)
# print the JSON string representation of the object
print(IncidentStatus.to_json())

# convert the object into a dict
incident_status_dict = incident_status_instance.to_dict()
# create an instance of IncidentStatus from a dict
incident_status_from_dict = IncidentStatus.from_dict(incident_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


