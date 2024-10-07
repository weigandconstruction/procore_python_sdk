# Project1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**name** | **str** | The name of the Project | [optional] 
**is_demo** | **bool** | Indicates whether this is a test project or not | [optional] 
**parent_job_id** | **int** | Identifier for the parent job | [optional] 
**display_name** | **str** | The display name for the Project | [optional] 
**project_number** | **str** | The Project number | [optional] 
**address** | **str** | The street address for the Project | [optional] 
**city** | **str** | The city in which the Project is located | [optional] 
**state_code** | **str** | The state code for the Project (ISO-3166 Alpha-2 format) | [optional] 
**country_code** | **str** | The country code for the Project (ISO-3166 Alpha-2 format) | [optional] 
**zip** | **str** | The postal code for the Project | [optional] 
**county** | **str** | The county in which the Project is located | [optional] 
**time_zone** | **str** | The timezone the Project is located in | [optional] 
**latitude** | **float** | The geographic coordinate that specifies the north–south position of the Project on the Earth&#39;s surface. | [optional] 
**longitude** | **float** | The geographic coordinate that specifies the east–west position of the Project on the Earth&#39;s surface. | [optional] 
**stage** | **str** | The name of the Project stage | [optional] 
**project_stage** | [**ProjectStage**](ProjectStage.md) |  | [optional] 
**project_template** | [**ProjectTemplate**](ProjectTemplate.md) |  | [optional] 
**phone** | **str** | The telephone number for the Project | [optional] 
**created_at** | **datetime** | The date and time the Project was created | [optional] 
**updated_at** | **datetime** | The date and time the Project was last updated | [optional] 
**active** | **bool** | The active status for the Project | [optional] 
**origin_id** | **str** | An external third-party identifier for the Project | [optional] 
**origin_data** | **str** | An external third-party data string associated with the Project | [optional] 
**origin_code** | **str** | An external third-party code associated with the Project | [optional] 
**owners_project_id** | **int** | A linked identifier for the Owner&#39;s Project | [optional] 
**total_value** | **float** | The total amount of construction work performed, planned, or put in place during the project. Note: this field is a replacement to estimated_value and will mirror its value. | [optional] 
**store_number** | **str** | The store number for the Project | [optional] 
**accounting_project_number** | **str** | The accounting project number for the Project | [optional] 
**designated_market_area** | **str** | The designated market area the Project is located in | [optional] 
**project_region_id** | **int** | The region identifier for the Project | [optional] 
**project_bid_type_id** | **int** | The Bid Type identifier for the Project | [optional] 
**project_owner_type_id** | **int** | The Owner Type identifier for the Project | [optional] 
**photo_id** | **int** | The unique identifier for the Project Photo | [optional] 
**start_date** | **date** | The start date for the project | [optional] 
**completion_date** | **date** | The completion date for the project | [optional] 
**estimated_value** | **float** | The Estimated Value of the project. Note: this field is now deprecated and will mirror the value of total_value until it is no longer supported. | [optional] 
**fax** | **str** | The fax number for the Project | [optional] 
**company** | [**ProjectCompany**](ProjectCompany.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project1 import Project1

# TODO update the JSON string below
json = "{}"
# create an instance of Project1 from a JSON string
project1_instance = Project1.from_json(json)
# print the JSON string representation of the object
print(Project1.to_json())

# convert the object into a dict
project1_dict = project1_instance.to_dict()
# create an instance of Project1 from a dict
project1_from_dict = Project1.from_dict(project1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


