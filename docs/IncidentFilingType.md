# IncidentFilingType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Incident Filing Type ID | [optional] 
**name** | **str** | Incident Filing Type Name | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**severity_level** | [**SeverityLevel**](SeverityLevel.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.incident_filing_type import IncidentFilingType

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentFilingType from a JSON string
incident_filing_type_instance = IncidentFilingType.from_json(json)
# print the JSON string representation of the object
print(IncidentFilingType.to_json())

# convert the object into a dict
incident_filing_type_dict = incident_filing_type_instance.to_dict()
# create an instance of IncidentFilingType from a dict
incident_filing_type_from_dict = IncidentFilingType.from_dict(incident_filing_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


