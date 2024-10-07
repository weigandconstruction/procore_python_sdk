# IncidentAttachment1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**name** | **str** | Filename | [optional] 
**content_type** | **str** |  | [optional] 
**viewable_document_id** | **int** | Viewable document ID | [optional] 

## Example

```python
from procore_sdk.models.incident_attachment1 import IncidentAttachment1

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentAttachment1 from a JSON string
incident_attachment1_instance = IncidentAttachment1.from_json(json)
# print the JSON string representation of the object
print(IncidentAttachment1.to_json())

# convert the object into a dict
incident_attachment1_dict = incident_attachment1_instance.to_dict()
# create an instance of IncidentAttachment1 from a dict
incident_attachment1_from_dict = IncidentAttachment1.from_dict(incident_attachment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


