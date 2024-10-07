# IncidentNormalAllOfNearMissesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Incident Record ID | [optional] 
**number** | **int** | The number of the Record | [optional] 
**full_number** | **str** | The Incident Number combined with the Record Number | [optional] 
**incident_id** | **int** | The id of the Incident to which the record belongs | [optional] 
**recordable** | **bool** | Indicates whether the Incident Record is recordable | [optional] 
**type** | **str** | The type of incident record (environmental, injury, near_miss, property_damage) | [optional] 
**incident_title** | **str** | The title of the Incident to which the record belongs | [optional] 
**incident_private** | **bool** | Indicates whether the Incident to which the record belongs is private | [optional] 
**summary** | **str** | Summary combining the affliction type, body part affected, and source of harm. | [optional] 
**description_plain_text** | **str** | Description of event | [optional] 
**description** | **str** | Description of event in Rich Text format | [optional] 
**affected_company** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**managed_equipment** | [**IncidentNormalAllOfEnvironmentalsInnerAllOfManagedEquipment**](IncidentNormalAllOfEnvironmentalsInnerAllOfManagedEquipment.md) |  | [optional] 
**incident_created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**work_activity** | [**WorkActivity**](WorkActivity.md) |  | [optional] 
**affected_party** | [**Party**](Party.md) |  | [optional] 
**affected_person** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**harm_source** | [**HarmSource1**](HarmSource1.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.incident_normal_all_of_near_misses_inner import IncidentNormalAllOfNearMissesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentNormalAllOfNearMissesInner from a JSON string
incident_normal_all_of_near_misses_inner_instance = IncidentNormalAllOfNearMissesInner.from_json(json)
# print the JSON string representation of the object
print(IncidentNormalAllOfNearMissesInner.to_json())

# convert the object into a dict
incident_normal_all_of_near_misses_inner_dict = incident_normal_all_of_near_misses_inner_instance.to_dict()
# create an instance of IncidentNormalAllOfNearMissesInner from a dict
incident_normal_all_of_near_misses_inner_from_dict = IncidentNormalAllOfNearMissesInner.from_dict(incident_normal_all_of_near_misses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


