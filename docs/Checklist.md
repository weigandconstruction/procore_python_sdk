# Checklist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**list_template_id** | **int** | Checklist Template ID from which this Checklist was created | [optional] 
**list_template_name** | **str** | Current name of the Checklist Template from which this Checklist was created | [optional] 
**number** | **int** | Number | [optional] 
**status** | **str** | Status | [optional] 
**location** | [**Location8**](Location8.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**closed_at** | **datetime** | Timestamp of when inspection was closed | [optional] 
**drawing_ids** | **List[int]** | Array of Drawing IDs | [optional] 
**current_drawing_revision_ids** | **List[int]** | Array of Current Drawing Revision IDs | [optional] 
**description** | **str** | Description | [optional] 
**deleted** | **bool** | Indicates whether this Checklist has been deleted | [optional] 
**due_at** | **datetime** | Timestamp indicating when the Inspection is due | [optional] 
**identifier** | **str** | Identifier | [optional] 
**inspection_date** | **date** | Date that the inspection was performed | [optional] 
**inspection_type** | [**InspectionType1**](InspectionType1.md) |  | [optional] 
**private** | **bool** | Indicates whether this Checklist is private | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**closed_by** | [**ChecklistClosedBy**](ChecklistClosedBy.md) |  | [optional] 
**responsible_contractor** | [**ChecklistResponsibleContractor**](ChecklistResponsibleContractor.md) |  | [optional] 
**point_of_contact** | [**ChecklistClosedBy**](ChecklistClosedBy.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**inspectors** | [**List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy]**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) | Inspectors | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy]**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) | Distribution Members | [optional] 
**signature_requests** | [**List[ChecklistSignatureRequest]**](ChecklistSignatureRequest.md) | Checklist Signature Requests | [optional] 
**managed_equipment_id** | **int** | Managed Equipment ID | [optional] 
**specification_section** | [**ChecklistSpecificationSection**](ChecklistSpecificationSection.md) |  | [optional] 
**attachments** | [**List[ChecklistInspectionAttachment]**](ChecklistInspectionAttachment.md) | Attachments | [optional] 
**conforming_item_count** | **int** | Number of Checklist Items with a status of &#x60;yes&#x60; | [optional] 
**deficient_item_count** | **int** | Number of Checklist Items with a status of &#x60;no&#x60; | [optional] 
**not_applicable_item_count** | **int** | Number of Checklist Items with a status of &#x60;n/a&#x60; | [optional] 
**neutral_item_count** | **int** | Number of Checklist Items with a status of &#x60;neutral&#x60; | [optional] 
**inspected_item_count** | **int** | Number of Checklist Items that have been inspected | [optional] 
**observations_count** | **int** | Number of Observations from this Checklist | [optional] 
**closed_observations_count** | **int** | Number of closed Observations pertaining to the Checklist | [optional] 
**item_count** | **int** | Number of Checklist Items within the Checklist | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**template_id** | **int** | Template ID | [optional] 
**overdue** | **bool** | Checklist List overdue flag | [optional] 

## Example

```python
from procore_sdk.models.checklist import Checklist

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist from a JSON string
checklist_instance = Checklist.from_json(json)
# print the JSON string representation of the object
print(Checklist.to_json())

# convert the object into a dict
checklist_dict = checklist_instance.to_dict()
# create an instance of Checklist from a dict
checklist_from_dict = Checklist.from_dict(checklist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


