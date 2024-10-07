# RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The record type, i.e. &#39;injury&#39;, &#39;near_miss&#39;, &#39;environmental&#39;, or &#39;property_damage&#39; | [optional] 
**estimated_cost_impact** | **str** | Estimated cost impact of the record | [optional] 
**responsible_company** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**id** | **int** | Incident Record ID | [optional] 
**number** | **int** | The number of the Record | [optional] 
**full_number** | **str** | The Incident Number combined with the Record Number | [optional] 
**incident_id** | **int** | The id of the Incident to which the record belongs | [optional] 
**recordable** | **bool** | Indicates whether the Incident Record is recordable | [optional] 
**incident_title** | **str** | The title of the Incident to which the record belongs | [optional] 
**incident_private** | **bool** | Indicates whether the Incident to which the record belongs is private | [optional] 
**summary** | **str** | Summary combining the affliction type, body part affected, and source of harm. | [optional] 
**description_plain_text** | **str** | Description of event | [optional] 
**description** | **str** | Description of event in Rich Text format | [optional] 
**affected_company** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**managed_equipment** | [**RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInnerAllOfManagedEquipment**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInnerAllOfManagedEquipment.md) |  | [optional] 
**incident_created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**work_activity** | [**WorkActivity1**](WorkActivity1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_incidents_property_damages_get200_response_inner_instance = RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_incidents_property_damages_get200_response_inner_dict = rest_v10_projects_project_id_incidents_property_damages_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner from a dict
rest_v10_projects_project_id_incidents_property_damages_get200_response_inner_from_dict = RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.from_dict(rest_v10_projects_project_id_incidents_property_damages_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


