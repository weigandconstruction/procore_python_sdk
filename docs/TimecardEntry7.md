# TimecardEntry7

Timecard Entry object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_id** | **int** | The ID of the Party of the Timecard Entry | [optional] 
**hours** | **str** | The Hours of the Timecard Entry | 
**billable** | **bool** | The Billable status of the Timecard Entry | [optional] [default to False]
**var_date** | **date** | The Date of the Timecard Entry | 
**description** | **str** | The Description of the Timecard Entry | [optional] 
**timecard_time_type_id** | **int** | The ID of the Timecard Time Type of the Timecard Entry | [optional] 
**cost_code_id** | **int** | The ID of the Cost Code of the Timecard Entry | [optional] 
**login_information_id** | **int** | The ID of the Login Information of the Timecard Entry | [optional] 
**origin_id** | **int** | ID of related external data | [optional] 
**origin_data** | **str** | Value of related external data | [optional] 
**line_item_type_id** | **int** | The ID of the Line Item Type of the Timecard Entry | [optional] 
**clock_in_time** | **str** | The datetime a timecard clock in was punched | [optional] 
**clock_out_time** | **str** | The datetime a timecard clock out was punched | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry7 import TimecardEntry7

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry7 from a JSON string
timecard_entry7_instance = TimecardEntry7.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry7.to_json())

# convert the object into a dict
timecard_entry7_dict = timecard_entry7_instance.to_dict()
# create an instance of TimecardEntry7 from a dict
timecard_entry7_from_dict = TimecardEntry7.from_dict(timecard_entry7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


