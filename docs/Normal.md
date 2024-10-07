# Normal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**accounting_project_number** | **str** | The accounting project number for the Project | [optional] 
**active** | **bool** | The active status for the Project | [optional] 
**address** | **str** | The street address for the Project | [optional] 
**city** | **str** | The city in which the Project is located | [optional] 
**company** | [**ProjectCompany**](ProjectCompany.md) |  | [optional] 
**completion_date** | **date** | The completion date for the project | [optional] 
**country_code** | **str** | The country code for the Project (ISO-3166 Alpha-2 format) | [optional] 
**county** | **str** | The county in which the Project is located | [optional] 
**created_at** | **datetime** | The date and time the Project was created | [optional] 
**custom_fields** | [**NormalCustomFields**](NormalCustomFields.md) |  | [optional] 
**designated_market_area** | **str** | The designated market area the Project is located in | [optional] 
**display_name** | **str** | The display name for the Project | [optional] 
**estimated_value** | **float** | The Estimated Value of the project. Note: this field is now deprecated and will mirror the value of total_value until it is no longer supported. | [optional] 
**is_demo** | **bool** | Indicates whether this is a test project or not | [optional] 
**latitude** | **float** | The geographic coordinate that specifies the north–south position of the Project on the Earth&#39;s surface. | [optional] 
**longitude** | **float** | The geographic coordinate that specifies the east–west position of the Project on the Earth&#39;s surface. | [optional] 
**name** | **str** | The name of the Project | [optional] 
**origin_code** | **str** | An external third-party code associated with the Project | [optional] 
**origin_data** | **str** | An external third-party data string associated with the Project | [optional] 
**origin_id** | **str** | An external third-party identifier for the Project | [optional] 
**owners_project_id** | **int** | A linked identifier for the Owner&#39;s Project | [optional] 
**parent_job_id** | **int** | Identifier for the parent job | [optional] 
**phone** | **str** | The telephone number for the Project | [optional] 
**photo_id** | **int** | The unique identifier for the Project Photo | [optional] 
**project_bid_type_id** | **int** | The Bid Type identifier for the Project | [optional] 
**project_number** | **str** | The Project number | [optional] 
**project_owner_type_id** | **int** | The Owner Type identifier for the Project | [optional] 
**project_region_id** | **int** | The region identifier for the Project | [optional] 
**project_stage** | [**ProjectStage**](ProjectStage.md) |  | [optional] 
**project_template** | [**ProjectTemplate**](ProjectTemplate.md) |  | [optional] 
**start_date** | **date** | The start date for the project | [optional] 
**state_code** | **str** | The state code for the Project (ISO-3166 Alpha-2 format) | [optional] 
**store_number** | **str** | The store number for the Project | [optional] 
**time_zone** | **str** | The timezone the Project is located in | [optional] 
**total_value** | **float** | The total amount of construction work performed, planned, or put in place during the project. Note: this field is a replacement to estimated_value and will mirror its value. | [optional] 
**updated_at** | **datetime** | The date and time the Project was last updated | [optional] 
**zip** | **str** | The postal code for the Project | [optional] 

## Example

```python
from procore_sdk.models.normal import Normal

# TODO update the JSON string below
json = "{}"
# create an instance of Normal from a JSON string
normal_instance = Normal.from_json(json)
# print the JSON string representation of the object
print(Normal.to_json())

# convert the object into a dict
normal_dict = normal_instance.to_dict()
# create an instance of Normal from a dict
normal_from_dict = Normal.from_dict(normal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


