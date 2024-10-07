# RestV10ProjectsProjectIdIncidentsConfigurationPatchRequestConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_by_default** | **bool** | Indicates whether or not Incidents are private by default | [optional] 
**default_distribution_ids** | **List[int]** | User IDs in the default distribution list | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_configuration_patch_request_configuration import RestV10ProjectsProjectIdIncidentsConfigurationPatchRequestConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsConfigurationPatchRequestConfiguration from a JSON string
rest_v10_projects_project_id_incidents_configuration_patch_request_configuration_instance = RestV10ProjectsProjectIdIncidentsConfigurationPatchRequestConfiguration.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsConfigurationPatchRequestConfiguration.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_configuration_patch_request_configuration_dict = rest_v10_projects_project_id_incidents_configuration_patch_request_configuration_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsConfigurationPatchRequestConfiguration from a dict
rest_v10_projects_project_id_incidents_configuration_patch_request_configuration_from_dict = RestV10ProjectsProjectIdIncidentsConfigurationPatchRequestConfiguration.from_dict(rest_v10_projects_project_id_incidents_configuration_patch_request_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


