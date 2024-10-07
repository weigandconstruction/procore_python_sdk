# ProjectIncidentConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | [optional] 
**private_by_default** | **bool** | Ensures that all Incidents are private by default | [optional] 
**default_distribution** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Users in the default distribution list | [optional] 

## Example

```python
from procore_sdk.models.project_incident_configuration import ProjectIncidentConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIncidentConfiguration from a JSON string
project_incident_configuration_instance = ProjectIncidentConfiguration.from_json(json)
# print the JSON string representation of the object
print(ProjectIncidentConfiguration.to_json())

# convert the object into a dict
project_incident_configuration_dict = project_incident_configuration_instance.to_dict()
# create an instance of ProjectIncidentConfiguration from a dict
project_incident_configuration_from_dict = ProjectIncidentConfiguration.from_dict(project_incident_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


