# IncidentAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**name** | **str** | Filename | [optional] 
**content_type** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.incident_attachment import IncidentAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentAttachment from a JSON string
incident_attachment_instance = IncidentAttachment.from_json(json)
# print the JSON string representation of the object
print(IncidentAttachment.to_json())

# convert the object into a dict
incident_attachment_dict = incident_attachment_instance.to_dict()
# create an instance of IncidentAttachment from a dict
incident_attachment_from_dict = IncidentAttachment.from_dict(incident_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


