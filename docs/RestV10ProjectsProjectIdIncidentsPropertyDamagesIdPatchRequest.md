# RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_damage** | [**IncidentPropertyDamageUpdateParameters**](IncidentPropertyDamageUpdateParameters.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_id_patch_request import RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest from a JSON string
rest_v10_projects_project_id_incidents_property_damages_id_patch_request_instance = RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_property_damages_id_patch_request_dict = rest_v10_projects_project_id_incidents_property_damages_id_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest from a dict
rest_v10_projects_project_id_incidents_property_damages_id_patch_request_from_dict = RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest.from_dict(rest_v10_projects_project_id_incidents_property_damages_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


