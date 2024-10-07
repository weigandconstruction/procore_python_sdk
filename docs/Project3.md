# Project3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**logo_url** | **str** | The URL for the Project logo | [optional] 
**name** | **str** | The name for the Project | [optional] 
**is_demo** | **bool** | Indicates if the project is a test project | [optional] 
**template** | **bool** | Indicates if the project is a template project | [optional] 
**display_name** | **str** | The display name for the Project | [optional] 
**project_number** | **str** | The Project number | [optional] 
**address** | **str** | The street address for the Project | [optional] 
**city** | **str** | The city in which the Project is located | [optional] 
**state_code** | **str** | The state code for the Project (ISO-3166 Alpha-2 format) | [optional] 
**country_code** | **str** | The country code for the Project (ISO-3166 Alpha-2 format) | [optional] 
**zip** | **str** | The postal code for the Project | [optional] 
**time_zone** | **str** | The timezone in which the Project is located | [optional] 
**tz_name** | **str** | The tz-database version of the timezone for the Project | [optional] 
**latitude** | **float** | The geographic coordinate that specifies the north–south position of the Project on the Earth&#39;s surface. | [optional] 
**longitude** | **float** | The geographic coordinate that specifies the east–west position of the Project on the Earth&#39;s surface. | [optional] 
**county** | **str** | The county in which the Project is located | [optional] 
**parent_job_id** | **int** | Unique identifier for the Parent Job | [optional] 
**description** | **str** | Project description | [optional] 
**square_feet** | **int** | The total square footage for the Project | [optional] 
**start_date** | **date** | The date that the contract for the project is signed. Note: this field is a replacement to estimated_start_date and will mirror its value. | [optional] 
**completion_date** | **date** | The date that all parties agree the project meets or must meet “substantial completion”. Note: this field is a replacement to estimated_completion_date and will mirror its value. | [optional] 
**total_value** | **float** | The total amount of construction work performed, planned, or put in place during the project. Note: this field is a replacement to estimated_value and will mirror its value. | [optional] 
**store_number** | **str** | The store number for the Project | [optional] 
**accounting_project_number** | **str** | The accounting project number for the Project | [optional] 
**designated_market_area** | **str** | The designated market area the Project is located in | [optional] 
**warranty_start_date** | **date** | The start date for the Project Warranty | [optional] 
**warranty_end_date** | **date** | The end date for the Project Warranty | [optional] 
**active** | **bool** | The active status for the Project | [optional] 
**flag** | **str** | The Project flag (Red, Yellow, or Green) | [optional] 
**phone** | **str** | The telephone number for the Project | [optional] 
**public_notes** | **str** | Public notes on the Project | [optional] 
**actual_start_date** | **date** | The actual start date for the Project | [optional] 
**projected_finish_date** | **date** | The projected finish date for the Project | [optional] 
**created_at** | **datetime** | The date and time the Project was created | [optional] 
**updated_at** | **datetime** | The date and time the Project was last updated | [optional] 
**origin_id** | **str** | An external third-party identifier for the Project | [optional] 
**origin_data** | **str** | An external third-party data string associated with the Project | [optional] 
**origin_code** | **str** | An external third-party code associated with the Project | [optional] 
**standard_cost_code_list_id** | **int** |  | [optional] 
**is_erp_integrated** | **bool** | True if project is ERP integrated | [optional] 
**owners_project_id** | **int** | A linked identifier for the Owner&#39;s Project | [optional] 
**photo_id** | **int** | The unique identifier for the Project Photo | [optional] 
**inbound_email** | **str** | The inbound email address username suffix for the project. | [optional] 
**inbound_email_address** | **str** | The inbound email address for the project. | [optional] 
**estimated_start_date** | **date** | The Estimated Start Date of the Project Note: this field is now deprecated and will mirror the value of start_date until it is no longer supported. | [optional] 
**estimated_completion_date** | **date** | The Estimated Completion Date of the Project. Note: this field is now deprecated and will mirror the value of completion_date until it is no longer supported. | [optional] 
**estimated_value** | **float** | The Estimated Value of the project. Note: this field is now deprecated and will mirror the value of total_value until it is no longer supported. | [optional] 
**code** | **str** | The Code of the project. | [optional] 
**persistent_message** | [**ProjectPersistentMessage1**](ProjectPersistentMessage1.md) |  | [optional] 
**office** | [**ProjectOffice1**](ProjectOffice1.md) |  | [optional] 
**project_bid_type_id** | **int** | The identifier for the Project Bid Type | [optional] 
**project_bid_type** | [**ProjectBidType1**](ProjectBidType1.md) |  | [optional] 
**project_owner_type_id** | **int** | The identifier for the Project Owner Type | [optional] 
**project_owner_type** | [**ProjectOwnerType1**](ProjectOwnerType1.md) |  | [optional] 
**project_region_id** | **int** | The Project Region ID of the Project | [optional] 
**project_region** | [**ProjectRegion1**](ProjectRegion1.md) |  | [optional] 
**project_stage_id** | **int** | The identifier for the Project Stage | [optional] 
**project_stage** | [**ProjectStage**](ProjectStage.md) |  | [optional] 
**project_type** | [**ProjectType1**](ProjectType1.md) |  | [optional] 
**program** | [**ProjectProgram1**](ProjectProgram1.md) |  | [optional] 
**departments** | [**List[ProjectDepartment1]**](ProjectDepartment1.md) | An array of project departments | [optional] 
**company** | [**ProjectCompany2**](ProjectCompany2.md) |  | [optional] 
**dictionary_type** | **str** | Dictionary Type | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project3 import Project3

# TODO update the JSON string below
json = "{}"
# create an instance of Project3 from a JSON string
project3_instance = Project3.from_json(json)
# print the JSON string representation of the object
print(Project3.to_json())

# convert the object into a dict
project3_dict = project3_instance.to_dict()
# create an instance of Project3 from a dict
project3_from_dict = Project3.from_dict(project3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


