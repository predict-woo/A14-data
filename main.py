import streamlit as st
import pandas as pd
from components.reason_year_accident import main as reason_year_accident
from components.traffic_score import main as traffic_score
from components.reason_death_hurt import main as reason_death_hurt
from components.many_accidents import main as many_accidents
from components.crosswalk import main as crosswalk


def notion_callout(text, color="#ffcc00"):
    callout_html = f"""
    <div style='
        display: flex;
        align-items: center;
        padding: 1.2rem;
        margin: 1rem 0;
        background-color: rgb(241, 241, 239);;
        border-radius: 8px;
        word-break: keep-all;
        gap: 10px;
        '>
        <span style='font-size: 24px;'>💡</span>
        <div style='margin-left: 10px; font-size: 16px;'>
            {text}
        </div>
    </div>
    """
    st.markdown(callout_html, unsafe_allow_html=True)

def intro():
    html = """    
    <div style='
        display: flex;
        align-items: top;
        padding: 1.2rem;
        margin: 1rem 0;
        background-color: rgb(250, 243, 221);;
        border-radius: 8px;
        word-break: keep-all;
        gap: 10px;
        '>
        <span style='font-size: 24px;'>🙇</span>
        <div style='margin-left: 10px; font-size: 16px;'>
            <b>[데이터 분석 방향성]</b> <br>
            1. 대전광역시 교통 현황: <b>(1-1) 구별 분석 → (1-2) 지역별 분석</b>  <br>
            2. <b>(2-1) 신호등과 사고다발지 연관성</b> 분석 <br>
            3. 대전광역시 사고: <b>(3-1) 사고 유형, (3-2) 사고 원인</b> 분석 <br>
            <br>
            <b>[데이터 분석 배경]</b> <br>
            1) 대전광역시는 대중 교통 수단의 접근성이 낮고, 개인 승용차 이용이 편리한 도시 구조를 지니고 있습니다. <br>
            2) 최근 대전시는 2026년까지 교통사고 사망자수를 44명 이하로 감소시키겠다는 목표를 설정하였습니다. 이는 대전광역시가 교통사고 감소를 주 목적으로 삼고 있으며, 교통사고 감소에 대한 서비스 니즈가 있음을 짐작하게 합니다. <br>
            3) 대전광역시의 교통사고 현황 및 부상 정도를 다각도로 살펴보고, 교통사고 해결에 기여할 수 있는 서비스 아이디어로 발전시켜보고 싶었습니다. 
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Example usage

def main():

    st.title("데이터 시각화 미션")

    intro()
    
    

    notion_callout("<b>첫번째로 대전광역시 전반의 교통 안전지수가 어떠한지 파악</b>하기 위해, 대전광역시 구별 ‘교통 안전 지수’를 분석해보았습니다.")

    st.markdown("## 1-1. 대전광역시 구별 교통 안전 지수")

    st.write("\n\n")
    traffic_score()
    st.write("\n\n")

    st.markdown("""
    - 활용 데이터: [생활안전정보](https://www.safemap.go.kr/asds/safe.do#tab1) (대전-교통-2022년 기준, excel 파일 자체제작)
    - 분석 이유: 대전광역시 구별 교통 안전 지수 파악
        - **교통안전지수란?** 교통사고 빅데이터를 기반으로 기초지자체의 교통안전수준을 평가한 지수로써 보행자, 교통약자, 사업용차량, 자전거 등 6개 영역 18개 세부지표로 구성되어 취약 영역 파악 및 교통정책에 활용 가능한 지수
    - 시각화 툴: bar chart
    - 결과 해석:
        - 분석 결과 대전광역시 교통지수 - 4등급 3개, 3등급 1개, 2등급 1개
        - **전반적으로 교통 안전 지수 낮은 상황**
    """)



    notion_callout("분석 결과 <b>구체적인 지역별 사건 사고</b>가 어떤 추이일까 궁금하여 사고 다발 데이터를 바탕으로 위험도 지수, 사고건수, 사상자수, 사망자수, 중상자수, 경상자수, 부상신고자수를 파악해보았습니다.")

    st.markdown("## 1-2. 대전 지역별 사건 사고 분석")

    st.write("\n\n")
    m = many_accidents()
    st.write("\n\n")

    st.markdown("""
    - 활용 데이터: 사고다발지역데이터
    - 분석 이유: 지역별 사고 정도 (위험도 지수, 사고건수, 사상자수, 사망자수, 중상자수, 경상자수, 부상신고자수) 파악
        - 지수 설명
            - 위험도 지수: (사고 경중별 가중치 부여) 사망자수*5 + 중상자수*2 + 경상자수*1
            - *사상자수: 사망자수 + 중상자수 + 경상자수
    - 시각화 툴:
    - 결과 해석:
        - 대전 서구 둔산동 (둔산엔도내과의원) 부근에 가장 많은 사건 사고 발생
        - 지수별 사고 위험 TOP1 지역 분석
            - 위험도 지수: 대전 서구 둔산동 (문정네거리 부근), 대전 서구 둔산동 (둔산엔도내과의원 부근)
            - 사고건수: 대전 서구 둔산동 (둔산엔도내과의원)
            - 사상자수: 대전 서구 둔산동 (둔산엔도내과의원)
            - 사망자수: 대전 서구 둔산동 (문정네거리 부근)
            - 중상자수: 대전 서구 둔산동 (둔산엔도내과의원)
            - 경상자수, 부상신고자수는 한자리수라 제외
    """)

    notion_callout("<b>두번째로, 신호등이 설치된 곳에서도 사고가 많이 일어나고 있는 것일까요? 신호등이 본연의 역할을 수행하고 있는지</b> 알아보고 싶었습니다. ")

    st.markdown("## 2-1. 대전 지역별 신호등과 사고다발지 연관성 분석")
    st.write("\n\n")
    crosswalk(m)
    st.write("\n\n")
    st.markdown("""
    - 활용 데이터: 사고다발지역데이터, 대전 전체 횡단보도 및 신호등 데이터
    - 분석 이유: 횡단보도와 사고다발지의 연관성을 분석하기 위해 횡단보도 유무와 사고다발지의 연관성 분석
    - 시각화 툴: Heatmap
    - 결과 해석:
        - **신호등이 있는 횡단보도임에도 많은 사고 발생**
    """)

    notion_callout("<b>세번째로, 대전광역시 교통사고는 어떤 유형이 가장 빈번하게 발생</b>하는지 분석해보았습니다.")

    st.markdown("## 3-1. 사고 유형별 사망자수 비교")

    st.write("\n\n")
    reason_year_accident()
    st.write("\n\n")

    st.markdown("""
    - 활용 데이터: 2022년 교통사고 통계자료 ([대전의 통계](https://www.daejeon.go.kr/sta/StaStatisticsFldView.do?ntatcSeq=1442240988&menuSeq=180&colmn1Cont=&colmn2Cont=&boardId=normal_0009&pageIndex=1&searchCondition=TITLE&searchKeyword=%EA%B5%90%ED%86%B5%EC%82%AC%EA%B3%A0+%ED%86%B5%EA%B3%84#))
    - 분석 이유: 년도별 교통사고 주요 원인 분석
    - 시각화 툴: Line Chart
    - 결과 해석:
        - 2015년 이후 8년 연속 사망자수 연 6000건 초과
        - 유형: 안전운전불이행>**신호위반**>안전거리미확보>기타
    """)



    notion_callout("<b>대전광역시 교통사고의 사고 원인</b>도 분석해보았습니다.")

    st.markdown("## 3-2. 원인에 따른 사고 결과 비교")
    st.write("\n\n")
    reason_death_hurt()
    st.write("\n\n")
    st.markdown("""
    - 활용 데이터: 2022년 교통사고 통계자료 ([대전의 통계](https://www.daejeon.go.kr/sta/StaStatisticsFldView.do?ntatcSeq=1442240988&menuSeq=180&colmn1Cont=&colmn2Cont=&boardId=normal_0009&pageIndex=1&searchCondition=TITLE&searchKeyword=%EA%B5%90%ED%86%B5%EC%82%AC%EA%B3%A0+%ED%86%B5%EA%B3%84#))
    - 분석 이유: 사망자수, 부상자수 발생 원인 분석, 사망률 원인 분석
        - 사망률: 사망자수/(사망자수+부상자수)
    - 시각화 툴: Heatmap
    - 결과 해석:
        - 교통사고 사망과 부상의 가장 큰 원인은 **‘횡단중’**
        - **횡단 과정서 안전책 필요**
    """)


    notion_callout("""
    <b>결론 및 인사이트</b> <br> 
    -대전광역시 교통 안전은 다소 좋지 않은 편입니다. <br>
    -사고 유형의 주 원인으로 <b>신호위반이 있으며</b>, 교통 사고 방지를 위해 제작된 신호등은 제 역할을 수행하지 못하고 있습니다. <br>
    -사망과 부상은 ‘횡단’ 과정에서 가장 많이 발생합니다. 따라서 <b>횡단 과정서 안전책이 필요</b>합니다. """)

    st.write("\n")

    notion_callout("""
    <b>서비스 아이디어</b> <br>
    -보행자가 신호등이 있는 교차로에 접근했을 때, 빨간불이 초록불로 변하기까지의 잔여시간을 알려주는 웹앱 서비스를 제작해보고자 하였습니다.""")

if __name__ == '__main__':
    main()