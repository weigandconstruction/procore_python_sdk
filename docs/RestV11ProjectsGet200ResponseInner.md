# RestV11ProjectsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**accounting_project_number** | **str** | Accounting Project Number of the Project | [optional] 
**active** | **bool** | Project active status | [optional] 
**address** | **str** | Project address | [optional] 
**city** | **str** | Project city | [optional] 
**company** | [**ProjectCompany1**](ProjectCompany1.md) |  | [optional] 
**completion_date** | **date** | The date that all parties agree the project meets or must meet “substantial completion”. Note: this field is a replacement to estimated_completion_date and will mirror its value. | [optional] 
**country_code** | **str** | Project country code (ISO-3166 Alpha-2 format) | [optional] 
**county** | **str** | Project county | [optional] 
**created_at** | **datetime** | Project created at | [optional] 
**custom_fields** | [**NormalCustomFields**](NormalCustomFields.md) |  | [optional] 
**designated_market_area** | **str** | Designated Market Area of the Project | [optional] 
**display_name** | **str** | Project display name | [optional] 
**estimated_value** | **float** | The Estimated Value of the Project. Note: this field is now deprecated and will mirror the value of total_value until it is no longer supported. | [optional] 
**is_demo** | **bool** | Indicates whether this is a test project or not | [optional] 
**latitude** | **float** | Project latitude | [optional] 
**longitude** | **float** | Project longitude | [optional] 
**name** | **str** | Project name | [optional] 
**origin_code** | **str** | Project third party code | [optional] 
**origin_data** | **str** | Project third party data | [optional] 
**origin_id** | **str** | Project third party id | [optional] 
**owners_project_id** | **int** | Linked Owner&#39;s unique identifier for the Project | [optional] 
**parent_job_id** | **int** | Parent Job ID | [optional] 
**phone** | **str** | Project phone | [optional] 
**photo_id** | **int** | Project Photo Id | [optional] 
**project_bid_type_id** | **int** | The Bid Type identifier for the Project | [optional] 
**project_number** | **str** | Project number | [optional] 
**project_owner_type_id** | **int** | The Owner Type for the Project | [optional] 
**project_region_id** | **int** | The Region identifier for the Project | [optional] 
**project_stage** | [**ProjectStage1**](ProjectStage1.md) |  | [optional] 
**project_template** | [**ProjectTemplate**](ProjectTemplate.md) |  | [optional] 
**start_date** | **date** | The date that the contract for the project is signed. Note: this field is a replacement to estimated_start_date and will mirror its value. | [optional] 
**state_code** | **str** | Project state code (ISO-3166 Alpha-2 format) | [optional] 
**store_number** | **str** | Store Number of the Project | [optional] 
**time_zone** | **str** | The Timezone of the Project | [optional] 
**total_value** | **float** | The total amount of construction work performed, planned, or put in place during the project. Note: this field is a replacement to estimated_value and will mirror its value. | [optional] 
**updated_at** | **datetime** | Project updated at | [optional] 
**zip** | **str** | Project zip code | [optional] 
**actual_start_date** | **date** | Project actual start date | [optional] 
**departments** | [**List[ProjectDepartment]**](ProjectDepartment.md) | Array of project departments | [optional] 
**description** | **str** | Project description | [optional] 
**dictionary_type** | **str** | Dictionary Type | [optional] 
**estimated_completion_date** | **date** | The Estimated Completion Date of the Project. Note: this field is now deprecated and will mirror the value of completion_date until it is no longer supported. | [optional] 
**estimated_start_date** | **date** | The Estimated Start Date of the Project. Note: this field is now deprecated and will mirror the value of start_date until it is no longer supported. | [optional] 
**flag** | **str** | Project flag | [optional] 
**inbound_email** | **str** | The inbound email address username suffix for the project. | [optional] 
**logo_url** | **str** | Project logo url | [optional] 
**office** | [**ProjectOffice**](ProjectOffice.md) |  | [optional] 
**persistent_message** | [**ProjectPersistentMessage**](ProjectPersistentMessage.md) |  | [optional] 
**program** | [**ProjectProgram**](ProjectProgram.md) |  | [optional] 
**project_bid_type** | [**ProjectBidType**](ProjectBidType.md) |  | [optional] 
**project_owner_type** | [**ProjectOwnerType**](ProjectOwnerType.md) |  | [optional] 
**project_region** | [**ProjectRegion**](ProjectRegion.md) |  | [optional] 
**project_type** | [**ProjectType**](ProjectType.md) |  | [optional] 
**projected_finish_date** | **date** | Project finish date | [optional] 
**public_notes** | **str** | Project public notes | [optional] 
**square_feet** | **int** | Project square feet | [optional] 
**standard_cost_code_list_id** | **int** | The Standard Cost Code List identifier for the Project | [optional] 
**tz_name** | **str** | The tz-database version of the Timezone of the Project | [optional] 
**warranty_end_date** | **date** | Project warranty end date | [optional] 
**warranty_start_date** | **date** | Project warranty start date | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_get200_response_inner import RestV11ProjectsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsGet200ResponseInner from a JSON string
rest_v11_projects_get200_response_inner_instance = RestV11ProjectsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_get200_response_inner_dict = rest_v11_projects_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsGet200ResponseInner from a dict
rest_v11_projects_get200_response_inner_from_dict = RestV11ProjectsGet200ResponseInner.from_dict(rest_v11_projects_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


